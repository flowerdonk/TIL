package com.example.auction_practice.data.repository;

import com.example.auction_practice.data.entity.Seller;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SellerRepository extends JpaRepository<Seller, Long> {
}
