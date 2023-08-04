package com.example.sse_pub_sub.service;

import com.example.sse_pub_sub.entity.Alarm;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RedisPublishService {

    private RedisTemplate<String, Alarm> redisTemplate;

    /*
    * [publish]
    * 토픽에 알림을 보내면 변환한 후 전송
    * Config에서 설정해준 redisTemplate.converAndSend() 메서드 사용
    */
    public void publish(ChannelTopic topic, Alarm alarm) {
        redisTemplate.convertAndSend(topic.getTopic(), alarm);
    }
}
