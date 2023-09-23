import { StyleSheet, Text, View } from "react-native";

type PageGithubErrorProps = {
  messageError: string;
}

export function PageGithubError({ messageError }: PageGithubErrorProps) {
  return (
    <View style={styles.container}>
      <Text style={styles.message}>{messageError}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center"
  },
  message: {
    color: "#ec7070",
    fontSize: 24
  }
});
