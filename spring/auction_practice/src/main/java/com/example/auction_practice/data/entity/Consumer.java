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
public class Consumer {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "consumer_id")
    private Long id;

    @Column(nullable = false)
    private String nickname;

    @Column(nullable = false)
    private String image;

    private String addresss;

    @Column(nullable = false)
    private String login_id;

    @OneToMany(mappedBy = "consumer")
    @ToString.Exclude
    private List<Subscribe> subscribeList = new ArrayList<>();
}
