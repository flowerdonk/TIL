package com.example.redis_practice.entity;

import lombok.*;

import java.io.Serializable;

@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class ChatMessage implements Serializable {
    private String sender;
    private String context;
}
