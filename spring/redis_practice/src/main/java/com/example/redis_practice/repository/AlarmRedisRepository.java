package com.example.redis_practice.repository;

import com.example.redis_practice.entity.Alarm;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.concurrent.TimeUnit;

//@Component
@Repository
public class AlarmRedisRepository {

    private final RedisTemplate<String, Alarm> redisTemplate;

    public AlarmRedisRepository(RedisTemplate<String, Alarm> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public void save(String memberId, Alarm alarm) {
        redisTemplate.opsForList().leftPush(memberId, alarm);
        // TTL 설정 - 24시간
        redisTemplate.expire(memberId, 86400, TimeUnit.SECONDS);
    }

    public List<Alarm> findByMemberId(String memberId) {
        return redisTemplate.opsForList().range(memberId, 0, -1);
    }
}
