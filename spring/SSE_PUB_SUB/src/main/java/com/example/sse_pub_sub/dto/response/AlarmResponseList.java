package com.example.sse_pub_sub.dto.response;

import com.example.sse_pub_sub.entity.Alarm;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.List;
import java.util.stream.Collectors;

@Getter
@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class AlarmResponseList {

    private List<AlarmResponse> alarmResponseList;

    public AlarmResponseList(final List<Alarm> alarmList) {
        this.alarmResponseList = alarmList.stream()
                .map(AlarmResponse::toResponse)
                .collect(Collectors.toList());
    }
}
