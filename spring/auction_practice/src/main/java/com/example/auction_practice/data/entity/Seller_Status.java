package com.example.auction_practice.data.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@ToString
public class Seller_Status {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "seller_status_id")
    private Long id;

    @Column(nullable = false)
    private boolean is_out = false;
}
