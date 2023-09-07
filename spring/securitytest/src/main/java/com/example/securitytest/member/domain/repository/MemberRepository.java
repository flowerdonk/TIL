package com.example.securitytest.member.domain.repository;

import com.example.securitytest.member.domain.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {

    Member getByUuid(String uuid);
}
