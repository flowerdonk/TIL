package com.example.securitytest.member.controller;

import com.example.securitytest.member.dto.SignInRequestDto;
import com.example.securitytest.member.dto.SignInResponseDto;
import com.example.securitytest.member.dto.SignUpRequestDto;
import com.example.securitytest.member.dto.SignUpResponseDto;
import com.example.securitytest.member.service.SignService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;

@RestController
@RequestMapping("/api/member")
public class MemberController {

    private final Logger LOGGER = LoggerFactory.getLogger(MemberController.class);
    private final SignService signService;

    public MemberController(SignService signService) {
        this.signService = signService;
    }

    @PostMapping(value = "/sign-up")
    public ResponseEntity<Void> signUp(@RequestBody SignUpRequestDto requestDto) {
        signService.signUp(requestDto);
        return ResponseEntity.created(URI.create("/api/member")).build();
    }

    @PostMapping(value = "/sign-in")
    public SignInResponseDto signIn(@RequestBody SignInRequestDto requestDto)
            throws RuntimeException {
        LOGGER.info("[signIn] 로그인을 시도하고 있습니다. nickname : {}, pw : ****", requestDto.getNickname());
        SignInResponseDto signInResponseDto = signService.signIn(requestDto.getNickname(), requestDto.getPassword());

        LOGGER.info("[signIn] 정상적으로 로그인되었습니다. nickname : {}, token : {}", requestDto.getNickname(),
                signInResponseDto.getToken());
        return signInResponseDto;
    }
}
