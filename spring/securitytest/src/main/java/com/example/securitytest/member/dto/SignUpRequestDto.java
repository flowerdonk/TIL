package com.example.securitytest.member.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Getter
@Setter
@NoArgsConstructor
public class SignUpRequestDto {

    @NotBlank
    private String password;
    @NotBlank
    private String nickname;
    @NotNull
    private boolean isDeleted;
    private int height;
    private int weight;
    private int age;
    private int gender;
    private String fcmToken;

    @Builder
    public SignUpRequestDto(String password, String nickname, boolean isDeleted, int height, int weight, int age, int gender, String fcmToken) {
        this.password = password;
        this.nickname = nickname;
        this.isDeleted = isDeleted;
        this.height = height;
        this.weight = weight;
        this.age = age;
        this.gender = gender;
        this.fcmToken = fcmToken;
    }
}
