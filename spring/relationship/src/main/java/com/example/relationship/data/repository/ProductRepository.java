package com.example.relationship.data.repository;

import com.example.relationship.data.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> { // <대상 엔티티, 기본 타입>
}