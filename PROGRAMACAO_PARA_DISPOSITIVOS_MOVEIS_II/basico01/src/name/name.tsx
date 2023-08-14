import { Component, ReactNode, useState } from "react";
import { Container, Text } from "./name.styles";
import { Button } from "react-native";

type NameState = {
  name: string;
}

export class NameComponent extends Component<any, NameState> {

  constructor(props: any) {
    super(props);
    this.state = {
      name: "James"
    }

    this.changeName = this.changeName.bind(this);
  }


  changeName(name: string) {
    this.setState({
      name: name
    })
  }

  render(): ReactNode {
    return (
      <Container>
        <Button title="Entrar" onPress={() => this.changeName("Bob Johnson")} />
        <Text>{this.state.name}</Text>
      </Container>
    )
  }
}


export function NameFunction() {
  const [name, setName] = useState<string>("James")

  return (
    <Container>
      <Button title="Entrar" onPress={() => setName("Bob Johnson")} />
      <Text>{name}</Text>
    </Container>
  )
}
