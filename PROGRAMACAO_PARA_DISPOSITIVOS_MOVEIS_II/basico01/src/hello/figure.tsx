import { Component, ReactNode } from "react";
import { Image, Text, View } from "react-native";

type FigureProps = {
  width: number;
  height: number;
  text: string;
  url?: string;
}

export class Figure extends Component<FigureProps> {
  render(): ReactNode {
    return (
      <View>
        <Image source={{ uri: this.props.url }} style={{
          width: this.props.width,
          height: this.props.height
        }} />
        <Text>{this.props.text}</Text>
      </View>
    )
  }
}
