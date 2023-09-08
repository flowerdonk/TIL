package com.example.securitytest.member.dto;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class SignInResponseDto extends SignUpResponseDto{

    private String token;

    @Builder
    public SignInResponseDto(String uuid, String nickname, int height, int weight, int age, int gender, String fcmToken, String token) {
        super(uuid, nickname, height, weight, age, gender, fcmToken);
        this.token = token;
    }
}
