package com.example.sse_pub_sub.service;

import com.example.sse_pub_sub.entity.Alarm;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.data.redis.core.RedisOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RedisSubscribeService implements MessageListener {

    private final RedisTemplate<String, Alarm> redisTemplate;

    // ObjectMaper.readValue를 사용해서 JSON을 파싱해서 자바 객체(ChatMessage.Class)로 바꿔줌
    private final ObjectMapper mapper = new ObjectMapper();

    /*
     * [onMessage]
     * 메시지를 subscribe했을 때 수행할 메서드
     * 여기서 발행된 메시지를 읽어 추가 작업 수행
     */
    @Override
    public void onMessage(Message message, byte[] pattern) {
        try {
            Alarm alarm = mapper.readValue(message.getBody(), Alarm.class);
            redisTemplate.opsForList().rightPush("subscriber", alarm); // redisTemplate을 거쳐 레디스에 key(subscriber):list(alarm) 형태로 저장
            // 리스트로 잘 들어갔는지 확인
            RedisOperations<String, Alarm> operations = redisTemplate.opsForList().getOperations();
            System.out.println("subscriber alarm list = " + operations.opsForList().range("subscriber", 0, -1));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
