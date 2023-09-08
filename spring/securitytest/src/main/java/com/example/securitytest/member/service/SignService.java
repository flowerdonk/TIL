package com.example.securitytest.member.service;

import com.example.securitytest.config.security.JwtTokenProvider;
import com.example.securitytest.member.domain.entity.Member;
import com.example.securitytest.member.domain.repository.MemberRepository;
import com.example.securitytest.member.dto.SignInResponseDto;
import com.example.securitytest.member.dto.SignUpRequestDto;
import com.example.securitytest.member.dto.SignUpResponseDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;

@Service
public class SignService {

    private final Logger LOGGER = LoggerFactory.getLogger(SignService.class);
    private final MemberRepository memberRepository;
    private final JwtTokenProvider jwtTokenProvider;
    private final PasswordEncoder passwordEncoder;

    public SignService(MemberRepository memberRepository, JwtTokenProvider jwtTokenProvider, PasswordEncoder passwordEncoder) {
        this.memberRepository = memberRepository;
        this.jwtTokenProvider = jwtTokenProvider;
        this.passwordEncoder = passwordEncoder;
    }

    public void signUp(SignUpRequestDto requestDto) {

        Member savedMember = memberRepository.save(Member.builder()
                .nickname(requestDto.getNickname())
                .password(passwordEncoder.encode(requestDto.getPassword()))
                .roles(Collections.singletonList("ROLE_CONSUMER"))
                .build());

//        return SignUpResponseDto.toResponse(savedMember);
    }

    public SignInResponseDto signIn(String nickname, String password) throws RuntimeException {
        LOGGER.info("[getSignInResult] signDataHandler 로 회원 정보 요청");
        Member member = memberRepository.getByNickname(nickname);
        LOGGER.info("[getSignInResult] nickname : {}", nickname);

        LOGGER.info("[getSignInResult] 패스워드 비교 수행");
        if (!passwordEncoder.matches(password, member.getPassword())) {
            throw new RuntimeException();
        }
        LOGGER.info("[getSignInResult] 패스워드 일치");

        LOGGER.info("[getSignInResult] SignInResultDto 객체 생성");
        SignInResponseDto signInResponseDto = SignInResponseDto.builder()
                .token(jwtTokenProvider.createToken(String.valueOf(member.getUuid())))
                .build();

        LOGGER.info("[getSignInResult] SignInResultDto 객체에 값 주입");

        return signInResponseDto;
    }
}
