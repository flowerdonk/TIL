package com.example.sse_pub_sub.controller;


import com.example.sse_pub_sub.dto.response.AlarmResponseList;
import com.example.sse_pub_sub.service.AlarmService;
import com.example.sse_pub_sub.service.RedisPublishService;
import com.example.sse_pub_sub.service.RedisSubscribeService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.listener.RedisMessageListenerContainer;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/alarms")
public class AlarmController {

    // topic에 메시지 발행을 기다리는 리스너
    private final RedisMessageListenerContainer redisMessageListener;

    // 알림 서비스
    private final AlarmService alarmService;

    @PutMapping("/{topicName}")
    public ResponseEntity<Void> createTopic(@PathVariable String topicName) {
        final String topic = alarmService.createTopic(topicName);
        return ResponseEntity.created(URI.create("api/alarms/" + topic)).build();
    }

    @PostMapping("/{topicName}")
    public ResponseEntity<Void> pushAlarm(@PathVariable String topicName, @RequestParam(name = "sender") String sender, @RequestParam(name = "context") String context) {
        final String alarm = alarmService.pushAlarm(topicName, sender, context);
        return ResponseEntity.created(URI.create("api/alarms/" + alarm)).build();
    }

    @DeleteMapping("/{topicName}")
    public void deleteTopic(@PathVariable String topicName) {
        alarmService.deleteTopic(topicName);
    }

    @GetMapping("/{userId}")
    public ResponseEntity<AlarmResponseList> getAlarmList(@PathVariable String userId) {
        return ResponseEntity.ok(alarmService.getAlarmList(userId));
    }
}
