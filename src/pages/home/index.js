import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { Button, Image, ImageBackground, StyleSheet, Text, View } from 'react-native';
import { Tooltip } from 'react-native-elements';

import Menu from '../../components/Menu'


const image = require('../../assets/home.png');
const miles = require('../../assets/miles.png')

const Home = () => (
  <View style={styles.container}>
    <Menu />
    <ImageBackground source={image} style={styles.image}>
      <Tooltip popover={<Text>Info here</Text>}>
        <Image source={miles} style={styles.text} />
      </Tooltip>
    </ImageBackground>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column"
  },
  image: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center"
  },
  text: {
    position: 'absolute',
    top: '75%',
    alignSelf: 'flex-end',
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
  }
});


export default Home;