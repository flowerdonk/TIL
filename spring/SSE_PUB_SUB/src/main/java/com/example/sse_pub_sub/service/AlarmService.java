package com.example.sse_pub_sub.service;

import com.example.sse_pub_sub.dto.response.AlarmResponse;
import org.springframework.data.redis.listener.ChannelTopic;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;

public class AlarmService  {

    // topic 이름으로 topic 정보를 가져와 메시지를 발송할 수 있도록 Map에 저장
    private Map<String, ChannelTopic> channels;

    @PostConstruct
    public void init() {
        // topic 정보를 담을 Map을 초기화
        channels = new HashMap<>();
    }

    public AlarmResponse getAlarm(){

    }
}
