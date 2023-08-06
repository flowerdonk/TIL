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
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

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

    // 리포지토리 대신 템플릿 사용
    private final RedisTemplate<String, Alarm> redisTemplate;


    @PostConstruct
    public void init() { // topic 정보를 담을 Map을 초기화
        channels = new ConcurrentHashMap<>(); // topicName : ChannelTopic obj
    }

    public String createTopic(String topicName) { // 신규 Topic을 생성하고 Listener 등록 및 Topic Map에 저장
        ChannelTopic topic = new ChannelTopic(topicName); // 토픽 생성
        redisMessageListener.addMessageListener(redisSubscribeService, topic); // 리스너 등록
        channels.put(topicName, topic);
        return topicName;
    }

    public void pushAlarm(String topicName, String sender, String context) { // 알람 전송
        ChannelTopic topic = channels.get(topicName); // 토픽 객체 불러오기
        Alarm alarm = Alarm.builder().sender(sender).context(context).build(); // 알람 객체 생성
        redisPublishService.publish(topic, alarm); // 알람 전송
    }

    public void deleteTopic(String topicName) { // 토픽 제거
        ChannelTopic topic = channels.get(topicName); // 토픽 객체 불러오기
        redisMessageListener.removeMessageListener(redisSubscribeService, topic); // 토픽 제거
        channels.remove(topicName); // HashMap 제거
    }

    public AlarmResponseList getAlarmList(String memberId) { // 해당 유저의 알림 리스트 불러오기
        // 패턴 매칭 사용 -> member:memberId:alarm:*
        Set<String> keys = redisTemplate.keys("member:" + memberId + ":alarm:*"); // 해당 패턴을 가진 키 목록
        List<Alarm> alarmList = keys.stream().map(k -> redisTemplate.opsForValue().get(k)).collect(Collectors.toList()); // 해당 키의 알람 리스트 저장
        return new AlarmResponseList(alarmList);
    }
}
