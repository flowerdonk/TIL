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

@Getter
@Setter
@NoArgsConstructor
@ToString
@RedisHash(value = "alarm", timeToLive = 60) // value = keyspace, timeToLive = 초 단위 만료 시간
public class Alarm implements Serializable { // 필드 직렬화를 위한 인터페이스

    @Id // 최종적으로 key는 keyspace:id, 즉 alarm:00001 형식으로 설정됨
    private String id; // null값 저장 시 랜덤 스트링 값 설정
    private String sender; // 판매자일 경우 판매자 userId, 경매글일 경우 경매글 id
    private String context;
    @JsonSerialize(using = LocalDateTimeSerializer.class)
    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
    private LocalDateTime createdAt;

    @TimeToLive
    private Long expiration = 1L;

    @Builder
    public Alarm(String id, String sender, String context) {
        this.id = id;
        this.sender = sender;
        this.context = context;
        this.createdAt = LocalDateTime.now();
    }

}
