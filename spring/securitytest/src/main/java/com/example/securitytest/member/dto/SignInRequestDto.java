package com.example.securitytest.member.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.NotBlank;

@Getter
@Setter
@NoArgsConstructor
public class SignInRequestDto {

    @NotBlank
    private String password;
    @NotBlank
    private String nickname;

    @Builder
    public SignInRequestDto(String password, String nickname) {
        this.password = password;
        this.nickname = nickname;
    }
}