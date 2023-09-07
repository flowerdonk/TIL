package com.example.securitytest.member.service;

import com.example.securitytest.config.security.JwtTokenProvider;
import com.example.securitytest.member.domain.entity.Member;
import com.example.securitytest.member.domain.repository.MemberRepository;
import com.example.securitytest.member.dto.SignUpRequestDto;
import com.example.securitytest.member.dto.SignUpResponseDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

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

    public SignUpResponseDto signUp(SignUpRequestDto requestDto) {

        Member savedMember = memberRepository.save(Member.builder()
                .nickname(requestDto.getNickname())
                .password(requestDto.getPassword())
                .build());

        return SignUpResponseDto.toResponse(savedMember);
    }
}
