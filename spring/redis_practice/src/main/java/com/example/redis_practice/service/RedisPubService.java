package com.example.redis_practice.service;

import com.example.redis_practice.entity.ChatMessage;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RedisPubService {
    private final RedisTemplate<String, Object> redisTemplate;

    public void sendMessage(ChatMessage chatMessage) {
        System.out.println("RedisPubService.sendMessage");
        // Config에서 설정해준 redisTemplate.converAndSend() 메서드 사용
        redisTemplate.convertAndSend("topic1", chatMessage);
    }
}
