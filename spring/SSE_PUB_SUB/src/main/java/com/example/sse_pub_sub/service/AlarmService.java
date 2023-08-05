package com.example.sse_pub_sub.service;

import com.example.sse_pub_sub.dto.response.AlarmResponse;
import com.example.sse_pub_sub.dto.response.AlarmResponseList;
import com.example.sse_pub_sub.entity.Alarm;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.data.redis.listener.RedisMessageListenerContainer;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class AlarmService  {

    // topic에 메시지 발행을 기다리는 Listener
    private final RedisMessageListenerContainer redisMessageListener;

    // 발행 서비스
    private final RedisPublishService redisPublishService;

    // 구독 서비스
    private final RedisSubscribeService redisSubscribeService;

    // topic 이름으로 topic 정보를 가져와 메시지를 발송할 수 있도록 Map에 저장
    private Map<String, ChannelTopic> channels;

    private final RedisTemplate<String, Alarm> redisTemplate;

    @PostConstruct
    public void init() { // topic 정보를 담을 Map을 초기화
        channels = new HashMap<>(); // topicName : ChannelTopic obj
    }

    public String createTopic(String topicName) { // 신규 Topic을 생성하고 Listener 등록 및 Topic Map에 저장
        ChannelTopic topic = new ChannelTopic(topicName);
        redisMessageListener.addMessageListener(redisSubscribeService, topic);
        channels.put(topicName, topic);
        return topicName;
    }

    public String pushAlarm(String topicName, String sender, String context) {
        ChannelTopic topic = channels.get(topicName);
        Alarm alarm = Alarm.builder().id(null).sender(sender).context(context).build();
        redisPublishService.publish(topic, alarm);
        return alarm.getId();
    }

    public void deleteTopic(String topicName) {
        ChannelTopic topic = channels.get(topicName);
        redisMessageListener.removeMessageListener(redisSubscribeService, topic);
        channels.remove(topicName);
    }

    public AlarmResponseList getAlarmList(String userId){
        System.out.println("AlarmService.getAlarmList 진입");
        RedisOperations<String, Alarm> operations = redisTemplate.opsForList().getOperations();
        System.out.println("-----------");
        List<Alarm> alarmList = operations.opsForList().range("test", 0, -1);
        System.out.println("subscriber alarm list = " + alarmList);
        return new AlarmResponseList(alarmList);
    }

}
