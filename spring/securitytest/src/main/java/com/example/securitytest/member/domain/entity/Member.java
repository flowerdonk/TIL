package com.example.securitytest.member.domain.entity;

import com.example.securitytest.member.dto.SignUpRequestDto;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

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

    @Column(nullable = false)
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

    @ElementCollection(fetch = FetchType.EAGER)
    private List<String> roles = new ArrayList<>();

    public Collection<? extends GrantedAuthority> getAuthorities() {
        return this.roles.stream().map(SimpleGrantedAuthority::new).collect(Collectors.toList());
    }
//
//    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
//    @Override
//    public String getUsername() {
//        return this.uuid;
//    }
//
//     /* 계정이 만료되었는지 체크하는 로직
//      * 이 예제에서는 사용하지 않으므로 true 값 return
//      *
//      * @return true
//      */
//    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
//    @Override
//    public boolean isAccountNonExpired() {
//        return true;
//    }
//
//    /**
//     * 계정이 잠겼는지 체크하는 로직
//     * 이 예제에서는 사용하지 않으므로 true 값 return
//     *
//     * @return true
//     */
//    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
//    @Override
//    public boolean isAccountNonLocked() {
//        return true;
//    }
//
//    /**
//     * 계정의 패스워드가 만료되었는지 체크하는 로직
//     * 이 예제에서는 사용하지 않으므로 true 값 return
//     *
//     * @return true
//     */
//    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
//    @Override
//    public boolean isCredentialsNonExpired() {
//        return true;
//    }
//
//    /**
//     * 계정이 사용가능한지 체크하는 로직
//     * 이 예제에서는 사용하지 않으므로 true 값 return
//     *
//     * @return true
//     */
//    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
//    @Override
//    public boolean isEnabled() {
//        return true;
//    }

    @Builder
    public Member(long id, String password, String nickname, boolean isDeleted, int height, int weight, int age, int gender, String fcmToken, List<String> roles) {
        this.id = id;
        this.uuid = UUID.randomUUID().toString();
        this.password = password;
        this.nickname = nickname;
        this.isDeleted = isDeleted;
        this.height = height;
        this.weight = weight;
        this.age = age;
        this.gender = gender;
        this.fcmToken = fcmToken;
        this.roles = roles;
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
                .roles(requestDto.getRoles())
                .build();
    }
}
