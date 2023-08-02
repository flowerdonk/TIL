package com.example.redis_practice.service;

import com.example.redis_practice.entity.ChatMessage;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class RedisSubService implements MessageListener {
    public static List<String> messageList = new ArrayList<>();
    // ObjectMaper.readValue를 사용해서 JSON을 파싱해서 자바 객체(ChatMessage.Class)로 바꿔줌
    private final ObjectMapper mapper = new ObjectMapper();

    // 메시지를 subscribe했을 때 수행할 메서드
    /*
    * 여기서 발행된 메시지를 읽어 추가 작업 수행
    * */
    @Override
    public void onMessage(Message message, byte[] pattern) {
        System.out.println("RedisSubService.onMessage");
        try {
            ChatMessage chatMessage = mapper.readValue(message.getBody(), ChatMessage.class);
            // Redis에는 메시지가 저장되지 않아서 List에 추가해주고 출력하는 형태 -> DB 연결로 변경
            messageList.add(message.toString());

            System.out.println("받은 메시지 = " + message.toString());
            System.out.println("chatMessage.getSender() = " + chatMessage.getSender());
            System.out.println("chatMessage.getContext() = " + chatMessage.getContext());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
