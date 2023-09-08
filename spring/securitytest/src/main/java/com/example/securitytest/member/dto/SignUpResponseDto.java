package com.example.securitytest.member.dto;

import com.example.securitytest.member.domain.entity.Member;
import lombok.*;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class SignUpResponseDto {

    private String uuid;
    private String nickname;
    private int height;
    private int weight;
    private int age;
    private int gender;
    private String fcmToken;

//    @Builder
//    public SignUpResponseDto(String uuid, String nickname, int height, int weight, int age, int gender, String fcmToken) {
//        this.nickname = nickname;
//        this.height = height;
//        this.weight = weight;
//        this.age = age;
//        this.gender = gender;
//        this.fcmToken = fcmToken;
//    }
//
//    public static SignUpResponseDto toResponse(Member member) {
//        return SignUpResponseDto.builder()
//                .uuid(member.getUuid())
//                .nickname(member.getNickname())
//                .height(member.getHeight())
//                .weight(member.getWeight())
//                .age(member.getAge())
//                .gender(member.getGender())
//                .fcmToken(member.getFcmToken())
//                .build();
//    }
}
