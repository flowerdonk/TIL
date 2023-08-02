package com.example.redis_practice.controller;

import com.example.redis_practice.entity.ChatMessage;
import com.example.redis_practice.service.RedisPubService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class RedisController {
    private final RedisPubService redisPubService;

    @PostMapping("api/chat")
    public String pubSub(@RequestBody ChatMessage chatMessage) {
        System.out.println("RedisController.pubSub");
        // 메시지 보내기
        redisPubService.sendMessage(chatMessage);
        return "success";
    }


}
