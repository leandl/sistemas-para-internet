import { Image, StyleSheet, Text, View, FlatList } from "react-native";
import { useQuery } from "@tanstack/react-query";

import { GithubApiService, RepositoryGithub, UserGithub } from "../../services/github-api-service";
import { GithubApiServiceError } from "../../utils/errors/github-api-service-error";
import { RepositoryCard } from "./components/repository-card";
import { PageGithubSkeleton } from "./page-github.skeleton";
import { PageGithubError } from "./page-github.error";

type Repository = {
  name: string;
  description: string | null;
  language: string;
}

type User = {
  avatarURL: string;
  name: string;
  repos: Repository[];
}

type PageGithubProps = {
  username: string;
}

export function PageGithub({ username }: PageGithubProps) {

  const { data, isLoading, error } = useQuery<[UserGithub, RepositoryGithub[]], GithubApiServiceError, User>({
    queryKey: [username],
    queryFn: async () => {
      return Promise.all([
        GithubApiService.getUserInformation(username),
        GithubApiService.getReposByUsername(username),
      ])
    },
    select([user, repos]) {
      return {
        name: user.name,
        avatarURL: user.avatar_url,
        repos: repos.map((repo => ({
          description: repo.description,
          language: repo.language,
          name: repo.name
        })))
      }
    },
  });


  if (error) {
    return <PageGithubError messageError={error.message} />
  }

  if (isLoading) {
    return <PageGithubSkeleton />
  }



  return (
    <View style={styles.container}>
      <View style={styles.conatainerUserInformation}>
        <View style={styles.containerImage}>
          <Image
            style={styles.image}
            source={{ uri: data?.avatarURL }}
          />
        </View>
        <Text style={styles.name}>{data.name}</Text>
      </View>
      <FlatList
        style={styles.list}
        data={data.repos}
        keyExtractor={(repo) => repo.name}
        renderItem={({ item: repo }) => <RepositoryCard {...repo} />}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    paddingTop: 32,
    alignItems: "center"
  },
  conatainerUserInformation: {
    justifyContent: "center",
    alignItems: "center",
    gap: 8
  },
  containerImage: {
    width: 150,
    height: 150
  },
  image: {
    width: '100%',
    height: '100%',
    borderRadius: 50
  },
  name: {
    color: "#fff",
    fontSize: 22
  },
  list: {
    marginTop: 16,
    flex: 1,
    gap: 2,
  }
});
