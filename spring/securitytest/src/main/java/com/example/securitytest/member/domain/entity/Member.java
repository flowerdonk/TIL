package com.example.securitytest.member.domain.entity;

import com.example.securitytest.member.dto.SignUpRequestDto;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(nullable = false, unique = true)
    private String uuid;

    @Column(nullable = false, length = 20)
    private String password;

    @Column(nullable = false, length = 20)
    private String nickname;

    @Column(nullable = false)
    private boolean isDeleted;

    private int height;

    private int weight;

    private int age;

    private int gender;

    private String fcmToken;

    @Builder
    public Member(long id, String uuid, String password, String nickname, boolean isDeleted, int height, int weight, int age, int gender, String fcmToken) {
        this.id = id;
        this.uuid = uuid;
        this.password = password;
        this.nickname = nickname;
        this.isDeleted = isDeleted;
        this.height = height;
        this.weight = weight;
        this.age = age;
        this.gender = gender;
        this.fcmToken = fcmToken;
    }

    public static Member toEntity(SignUpRequestDto requestDto) {
        return Member.builder()
                .password(requestDto.getPassword())
                .nickname(requestDto.getNickname())
                .isDeleted(requestDto.isDeleted())
                .height(requestDto.getHeight())
                .weight(requestDto.getWeight())
                .age(requestDto.getAge())
                .gender(requestDto.getGender())
                .fcmToken(requestDto.getFcmToken())
                .build();
    }
}
