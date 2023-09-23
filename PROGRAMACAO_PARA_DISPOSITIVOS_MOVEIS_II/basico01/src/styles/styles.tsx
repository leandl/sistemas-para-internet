import { Component, ReactNode } from "react";
import { StyleSheet, Text, View } from "react-native";

const styles = StyleSheet.create({
  container: {
    marginTop: 40
  },
  textMain: {
    fontSize: 30,
    color: "#FF0000"
  },
  textAlign: {
    textAlign: "center"
  }
})

export class Styles extends Component {
  render(): ReactNode {
    return (
      <View style={styles.container}>
        <Text style={styles.textMain}>Eu sou texto 1</Text>
        <Text style={styles.textAlign}>Eu sou texto 2</Text>
        <Text>Eu sou texto 3</Text>
        <Text>Eu sou texto 4</Text>
      </View>
    );
  }
}
