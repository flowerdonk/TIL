package com.example.auction_practice.data.repository;

import com.example.auction_practice.data.entity.Consumer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ConsumerRepository extends JpaRepository<Consumer, Long> {
}
