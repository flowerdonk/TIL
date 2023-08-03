package com.example.sse_pub_sub.Config;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.datatype.jdk8.Jdk8Module;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import lombok.RequiredArgsConstructor;
import lombok.Value;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisClusterConfiguration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.util.StringUtils;

import java.util.Arrays;
import java.util.List;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class LettuceConnectionConfig {

//    @Value("${spring.redis.cluster.nodes}")
//    private String clusterNodes;
//    @Value("${spring.redis.cluster.max-redirects}")
//    private int maxRedirects;
//    @Value("${spring.redis.password}")
//    private String password;
//    private final SSERepository sseRepository;

    /*
     * Class <=> Json간 변환을 담당한다.
     *
     * json => object 변환시 readValue(File file, T.class)
     * => json File을 읽어 T 클래스로 변환 readValue(Url url, T.class)
     * => url로 접속하여 데이터를 읽어와 T 클래스로 변환 readValue(String string, T.class)
     * => string형식의 json데이터를 T 클래스로 변환
     *
     * object => json 변환시 writeValue(File file, T object)
     * => object를 json file로 변환하여 저장 writeValueAsBytes(T object)
     * => byte[] 형태로 object를 저장 writeValueAsString(T object)
     * => string 형태로 object를 json형태로 저장
     *
     * json을 포매팅(개행 및 정렬) writerWithDefaultPrettyPrint().writeValueAs... 를 사용하면 json파일이 포맷팅하여 저장된다.
     * object mapper로 date값 변환시 timestamp형식이 아니라 JavaTimeModule() 로 변환하여 저장한다.
     */
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
        mapper.registerModules(new JavaTimeModule(), new Jdk8Module());
        return mapper;
    }

//    @Bean
//    public RedisClusterConfiguration redisClusterConfiguration() {
//        List<String> clusterNodeList = Arrays.stream(StringUtils.split(clusterNodes, ','))
//                .map(String::trim)
//                .collect(Collectors.toList());
//        RedisClusterConfiguration redisClusterConfiguration = new RedisClusterConfiguration(clusterNodeList);
//        redisClusterConfiguration.setMaxRedirects(maxRedirects);
//        redisClusterConfiguration.setPassword(password);
//        return redisClusterConfiguration;
//    }

}
