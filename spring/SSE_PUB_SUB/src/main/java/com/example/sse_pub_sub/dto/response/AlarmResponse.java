package com.example.sse_pub_sub.dto.response;

import com.example.sse_pub_sub.entity.Alarm;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class AlarmResponse {

    private String sender;
    private String context;

    public static AlarmResponse toResponse(Alarm alarm) {
        return AlarmResponse.builder()
                .sender(alarm.getSender())
                .context(alarm.getContext())
                .build();
    }
}
