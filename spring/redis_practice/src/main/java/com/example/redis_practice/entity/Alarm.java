package com.example.redis_practice.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.redis.core.ListOperations;
import org.springframework.data.redis.core.RedisHash;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@ToString
@RedisHash(value = "alarm", timeToLive = 86400) // value = keyspace, timeToLive = 초 단위 만료 시간
public class Alarm { // redis 사용

    @Id // key, 최종적으로 key는 keyspace:id로 설정됨
    private String id; // MemberId
    private String sender;
    private String context;
    private LocalDateTime createdAt;

//    private ListOperations<>
    public Alarm(String id, String sender, String context, LocalDateTime createdAt) {
        this.id = id;
        this.sender = sender;
        this.context = context;
        this.createdAt = LocalDateTime.now();
    }
}
