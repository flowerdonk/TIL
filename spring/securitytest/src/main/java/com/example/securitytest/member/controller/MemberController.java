package com.example.securitytest.member.controller;

import com.example.securitytest.member.dto.SignUpRequestDto;
import com.example.securitytest.member.dto.SignUpResponseDto;
import com.example.securitytest.member.service.SignService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/member")
public class MemberController {

    private final Logger LOGGER = LoggerFactory.getLogger(MemberController.class);
    private final SignService signService;

    public MemberController(SignService signService) {
        this.signService = signService;
    }

    @PostMapping
    public ResponseEntity<SignUpResponseDto> signUp(@RequestBody SignUpRequestDto requestDto) {
        return ResponseEntity.ok(signService.signUp(requestDto));
    }
}
