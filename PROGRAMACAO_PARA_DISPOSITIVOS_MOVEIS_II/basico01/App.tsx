import { Component, ReactNode } from 'react';
import Hello from './src/hello/hello';
import { NameComponent, NameFunction } from './src/name/name';
import { Styles } from './src/styles/styles';


export default class App extends Component {
  render(): ReactNode {
    return (
      <Styles />
    );
  }
}
