package com.example.redis_practice.config;

import com.example.redis_practice.entity.ChatMessage;
import com.example.redis_practice.service.RedisSubService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.data.redis.listener.RedisMessageListenerContainer;
import org.springframework.data.redis.listener.adapter.MessageListenerAdapter;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfig {

    @Bean
    public RedisConnectionFactory redisConnectionFactory() {
        System.out.println("RedisConfig.redisConnectionFactory");
        return new LettuceConnectionFactory();
    }

    // redisTemplate 설정
    @Bean
    public RedisTemplate<String, Object> redisTemplate() {
        System.out.println("RedisConfig.redisTemplate");
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory());
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(new Jackson2JsonRedisSerializer<>(ChatMessage.class));
        return redisTemplate;
    }

    // 리스너 어댑터 설정
    /*
    * 스프링에서 비동기 메시지를 지원하는 마지막 컴포넌트
    * 정해진 채널로 들어온 메시지를 처리할 action을 정의
    * */
    @Bean
    MessageListenerAdapter messageListenerAdapter() {
        System.out.println("RedisConfig.messageListenerAdapter");
        return new MessageListenerAdapter(new RedisSubService());
    }

    // 컨테이너 설정
    /*
    * JMS template과 함께 스프링에서 JMS 메시징을 사용하는 핵심 컴포넌트.
    * MDP(message-driven POJO)를 사용하여 비동기 메시지를 받는데 사용.
    * 메시지의 수신관점에서 볼 때 필요
    * MessageListener를 생성하는데 사용
    * */
    @Bean
    RedisMessageListenerContainer redisContainer() {
        System.out.println("RedisConfig.redisContainer");
        RedisMessageListenerContainer container = new RedisMessageListenerContainer();
        container.setConnectionFactory(redisConnectionFactory());
        container.addMessageListener(messageListenerAdapter(), topic());
        return container;
    }

    // pub/sub 토픽 설정
    @Bean
    ChannelTopic topic() {
        System.out.println("RedisConfig.topic");
        return new ChannelTopic("topic1");
    }
}
