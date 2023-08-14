
import { Component, ReactNode } from 'react';
import { Text } from 'react-native';
import { Container } from './hello.styles';
import { Figure } from './figure';


export default class Hello extends Component {
  render(): ReactNode {
    return (
      <Container>
        <Text style={{
          color: "red",
          fontSize: 80
        }}>Hello World</Text>
        <Text>Este é um teste</Text>
        <Figure height={300} width={300} text='teste' url='https://cinepop.com.br/wp-content/uploads/2020/10/ariana-grande-2.jpg' />
      </Container>
    );
  }
}
