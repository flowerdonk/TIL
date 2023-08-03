package com.example.redis_practice.controller;

import com.example.redis_practice.entity.Alarm;
import com.example.redis_practice.repository.AlarmRedisRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class AlarmController {

    private final AlarmRedisRepository alarmRedisRepository;

    public AlarmController(AlarmRedisRepository alarmRedisRepository) {
        this.alarmRedisRepository = alarmRedisRepository;
    }

    @PostMapping("/alarms")
    public ResponseEntity<String> addAlarm(@RequestParam String memberId, @RequestBody Alarm alarm) {
        alarmRedisRepository.save(memberId, alarm);
        return ResponseEntity.ok("Alarm added successfully.");
    }

    @GetMapping("/alarms/{memberId}")
    public ResponseEntity<List<Object>> getAlarmsByMemberId(@PathVariable String memberId) {
        List<Object> alarms = alarmRedisRepository.findByMemberId(memberId);
        return ResponseEntity.ok(alarms);
    }
}
