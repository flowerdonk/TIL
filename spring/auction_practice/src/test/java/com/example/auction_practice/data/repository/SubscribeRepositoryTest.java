package com.example.auction_practice.data.repository;

import com.example.auction_practice.data.entity.Consumer;
import com.example.auction_practice.data.entity.Seller;
import com.example.auction_practice.data.entity.Subscribe;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.transaction.annotation.Transactional;

import static org.junit.jupiter.api.Assertions.*;

@Rollback(value = false)
@Transactional
@SpringBootTest
class SubscribeRepositoryTest {

    @Autowired
    private SubscribeRepository subscribeRepository;
    @Autowired
    ConsumerRepository consumerRepository;
    @Autowired
    SellerRepository sellerRepository;


    @Test
    void input() {
        // Given
        Consumer consumer = new Consumer();
        consumer.setNickname("wonjong");
        consumer.setAddresss("pungmudong");
        consumer.setImage("wonjong face");
        consumer.setLogin_id("david8318");
        Consumer savedConsumer = consumerRepository.save(consumer);

        Seller seller = new Seller();
        seller.setStore_name("yujin's store");
        seller.setPhone_number("8502");
        seller.setImage("yujin face");
        seller.setLogin_id("flowerdonk");
        Seller savedSeller = sellerRepository.save(seller);

        Subscribe subscribe = new Subscribe();
        subscribe.setConsumer(consumer);
        subscribe.setSeller(seller);
        Subscribe savedSubscribe = subscribeRepository.save(subscribe);

        seller.getSubscribeList().add(subscribe);
        consumer.getSubscribeList().add(subscribe);

        // When

        // Then
        System.out.println(consumer.getSubscribeList());
        System.out.println(seller.getSubscribeList());
    }

}