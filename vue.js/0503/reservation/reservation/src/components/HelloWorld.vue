<template>
  <div class="hello">
    <header>
      <h1>버튼 박스 제작</h1>
    </header>
    <section class="inner-wrapper">
      <div class="time-wrap">
        <h2>예약 페이지</h2>
        <h3>시간 선택</h3>
        <div class="timebox">
          <!-- 클래스 동적 바인딩
            :class="{'적용할 클래스' : 메소드(boolean값 리턴)}" -->
          <span class="timebtn" 
            v-for="(time, index) in times" 
            :key="index" 
            @click="selectTime(time)"
            :class="{'selected-timebtn': isSelected(time)}"
          >
            {{ time }}
          </span>
        </div>
        <hr>
        <p>선택 시간: {{ selectedTimes }}</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      times: ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
              "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
              "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
              ],
      selectedTimes: [],   
    }
  },
  methods: {
    // 버튼이 선택됐을 때 class를 동적으로 부여하기 위해 boolean값을 리턴
    isSelected(time) {
      if(this.selectedTimes.includes(time)){
        return true
      } else {
        return false
      }
    },
    selectTime(time) {
      if(this.selectedTimes.includes(time)){ // 이미 선택한 시간이면 삭제
        console.log('selectTime clicked!', time)
        const time_idx = this.selectedTimes.indexOf(time) // 방금 선택한 시간의 인덱스
        this.selectedTimes.splice(time_idx, 1) // (지울 인덱스, 지울 개수)
      } else { // 선택 안한 시간이면 추가
        if(this.selectedTimes.length === 5){
          alert('5 타임만 선택 가능합니다!')
          return
        }
        this.selectedTimes.push(time)
      }
    }
  },
}
</script>

<style scoped>
  .time-wrap {
    display: flex;
    flex-direction: column;
    align-content: center;
  }
  .timebox {
    display: flex;
    flex-wrap: wrap;
  }
  .timebtn {
    background-color: transparent;
    border: transparent;
    color: gray;
    font-size: 16px;
    margin-top: 2px;
    margin-bottom: 2px;
    width: 65px;
    text-align: center;
    cursor: pointer;
  }
  .selected-timebtn {
    background-color: darkgray;
    color: white;
    font-weight: bolder;
  }
</style>
