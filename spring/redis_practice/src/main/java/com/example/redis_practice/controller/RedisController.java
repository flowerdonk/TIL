package com.example.redis_practice.controller;

import com.example.redis_practice.entity.Alarm;
import com.example.redis_practice.entity.ChatMessage;
import com.example.redis_practice.service.RedisPubService;
import com.example.redis_practice.service.RedisSubService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.data.redis.listener.RedisMessageListenerContainer;
import org.springframework.web.bind.annotation.*;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api")
public class RedisController {
//    private final RedisPubService redisPubService;

//    @PostMapping("api/chat")
//    public String pubSub(@RequestBody ChatMessage chatMessage) {
//        System.out.println("RedisController.pubSub");
//        // 메시지 보내기
//        redisPubService.sendMessage(chatMessage);
//        return "success";
//    }

    // topic에 메시지 발행을 기다리는 Listener
    private final RedisMessageListenerContainer redisMessageListener;
    // 발행자
    private final RedisPubService redisPubService;
    // 구독자
    private final RedisSubService redisSubService;
    // topic 이름으로 topic 정보를 가져와 메시지를 발송할 수 있도록 Map에 저장
    private Map<String, ChannelTopic> channels;

    @PostConstruct
    public void init() {
        // topic 정보를 담을 Map을 초기화
        channels = new HashMap<>();
    }

    // 유효한 Topic 리스트 반환
    @GetMapping("/chats")
    public Set<String> findAllRoom() {
        return channels.keySet();
    }

    // 신규 Topic을 생성하고 Listener 등록 및 Topic Map에 저장
    @PutMapping("/chat/{topicName}")
    public void createChat(@PathVariable String topicName) {
        ChannelTopic channel = new ChannelTopic(topicName);
        redisMessageListener.addMessageListener(redisSubService, channel);
        channels.put(topicName, channel);
    }

    // 특정 Topic에 메시지 발행
    @PostMapping("/chat/{topicName}")
    public void pushMessage(@PathVariable String topicName, @RequestParam(name = "sender") String sender, @RequestParam(name = "context") String context) {
        ChannelTopic channel = channels.get(topicName);
        redisPubService.publish(channel, Alarm.builder().sender(sender).context(context).build());
    }

    // Topic 삭제 후 Listener 해제, Topic Map에서 삭제
    @DeleteMapping("/chat/{topicName}")
    public void deleteChat(@PathVariable String topicName) {
        ChannelTopic channel = channels.get(topicName);
        redisMessageListener.removeMessageListener(redisSubService, channel);
        channels.remove(topicName);
    }
}
