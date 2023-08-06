package com.example.sse_pub_sub.entity;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.datatype.jsr310.deser.LocalDateTimeDeserializer;
import com.fasterxml.jackson.datatype.jsr310.ser.LocalDateTimeSerializer;
import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;
import org.springframework.data.redis.core.TimeToLive;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@ToString
public class Alarm implements Serializable { // 필드 직렬화를 위한 인터페이스

    @Id
    private String id = UUID.randomUUID().toString(); // 랜덤 스트링 값 설정
    private String sender; // 판매자일 경우 판매자 userId, 경매글일 경우 경매글 id
    private String context;
    @JsonSerialize(using = LocalDateTimeSerializer.class)
    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
    private LocalDateTime createdAt;

    @Builder
    public Alarm(String sender, String context) {
        this.sender = sender;
        this.context = context;
        this.createdAt = LocalDateTime.now();
    }

}