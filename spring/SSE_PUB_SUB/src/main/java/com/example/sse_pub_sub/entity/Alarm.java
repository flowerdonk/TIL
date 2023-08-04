package com.example.sse_pub_sub.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;
import org.springframework.data.redis.core.RedisHash;

import java.io.Serializable;

@Getter
@Builder
@NoArgsConstructor
@ToString
@RedisHash(value = "alarm", timeToLive = 60) // value = keyspace, timeToLive = 초 단위 만료 시간
public class Alarm implements Serializable { // 필드 직렬화를 위한 인터페이스

    private String sender; // 판매자일 경우 판매자 userId, 경매글일 경우 경매글 id
    private String context;

    public Alarm(String sender, String context) {
        this.sender = sender;
        this.context = context;
    }
}
