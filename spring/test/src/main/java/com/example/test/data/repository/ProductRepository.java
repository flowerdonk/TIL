package com.example.test.data.repository;

import com.example.test.data.entity.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProductRepository extends JpaRepository<Product, Long> { // <대상 엔티티, 기본 타입>

    List<Product> findByName(String name, Sort sort);

    Page<Product> findByName(String name, Pageable pageable);
}