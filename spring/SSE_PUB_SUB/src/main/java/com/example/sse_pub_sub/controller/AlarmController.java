package com.example.sse_pub_sub.controller;


import com.example.sse_pub_sub.service.RedisPublishService;
import com.example.sse_pub_sub.service.RedisSubscribeService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.listener.RedisMessageListenerContainer;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/alarms")
public class AlarmController {

    // topic에 메시지 발행을 기다리는 리스너
    private final RedisMessageListenerContainer redisMessageListener;

    // 발행 서비스
    private final RedisPublishService redisPublishService;

    // 구독 서비스
    private final RedisSubscribeService redisSubscribeService;


}
