package com.example.securitytest.member.service;

import com.example.securitytest.member.domain.entity.Member;
import com.example.securitytest.member.domain.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@RequiredArgsConstructor
@Service
public class MemberDetailsService{

    private final Logger LOGGER = LoggerFactory.getLogger(MemberDetailsService.class);

    private final MemberRepository memberRepository;

//    @Override
    public Member loadUserByUsername(String username) throws UsernameNotFoundException {
        LOGGER.info("[loadUserByUsername] loadUserByUsername 수행. username : {}", username);
        return memberRepository.getByUuid(username);
    }

}