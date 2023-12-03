// main.js

// getter 학습하기

// 생성자 함수와 this 복습
// + JSDoc 주석 연습
/**
 * 생성자 함수를 통한 Dog 클래스의 인스턴스 생성 예제
 * @class
 */
class Dog {
  /**
   * Dog 클래스의 생성자 함수
   * @param {string} name - 개의 이름
   * @param {number} age - 개의 나이
   */
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  /**
   * 개가 짖는 소리를 출력하는 메서드
   */
  bark() {
    console.log('멍멍!');
  }
  /**
   * 개의 성인 여부를 확인하는 getter
   * (3살이면 성인으로 판단)
   * @returns {boolean} 개가 성인이면 true, 그렇지 않으면 false
   */
  get isAdult() {
    return this.age >=3;
  }
}

// Dog 생성자 함수를 호출하여 새로운 객체를 생성하고 초기화
const myDog = new Dog('멍멍이', 3);
// 새로운 객체 myDog를 출력
console.log(myDog); // Dog { name: '멍멍이', age: 3 }

// 개가 짖는 소리 출력
myDog.bark(); // 멍멍!

// 개의 성인 여부를 확인
console.log(myDog.isAdult); // true