package com.example.auction_practice.data.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
@ToString
public class Seller {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "seller_id")
    private Long id;

    @Column(nullable = false)
    private String store_name;

    @Column(nullable = false)
    private String image;

    private String phone_number;

    @Column(nullable = false)
    private String login_id;

    @OneToMany(mappedBy = "seller")
    @ToString.Exclude
    private List<Subscribe> subscribeList = new ArrayList<>();
}
