import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { Button, Image, ImageBackground, StyleSheet, Text, View } from 'react-native';
import { RectButton } from 'react-native-gesture-handler';
import Menu from '../../components/Menu'


const Home = () => {

    const navigation = useNavigation();

    function handleNavigateToPoints() {
        navigation.navigate('Points');
    }

    function handleNavigateToRegister() {
        navigation.navigate('Register');
    }

    return (
        <>
            <View style={styles.container}>
                <View style={styles.section}>
                    <View style={styles.textContainer}>
                        <Text style={styles.title}>
                            Para tornar sua experiência ainda mais incrível,
                            precisamos fazer algumas perguntinhas para te conhecer melhor e estarmos cada vez mais conectados 🧡
                        </Text>
                        <Text style={styles.text}>
                            Fique tranquilo, não vai levar mais que 2 minutos (:
                        </Text>
                    </View>
                    <View style={styles.buttonContainer}>
                        <RectButton style={styles.button}>
                            <Text style={styles.buttonText}>Iniciar</Text>
                        </RectButton>
                    </View>
                </View>
                <View style={styles.footer}>
                    
                </View>
            </View>
        </>

    );

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },

    menu: {
        flex: 1,
        marginTop: 40,
    },
    section: {
        flex: 3,
        justifyContent: 'center',
        alignItems: 'center',
        paddingTop: 30,
        margin:15,
    },
    box: {
        backgroundColor: '#28407C',
        width: '100%',
        height: 20,
        borderTopEndRadius: 15,
        borderTopStartRadius: 15,
    },

    textContainer: {
        flex: 1,
        width: 500,
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonContainer: {
        flex: 0.3,
        width: 500,
        justifyContent: 'center',
        alignItems: 'baseline',
        maxWidth: 260,
    },
    buttonText:{
        color: 'white',
    },


    title: {
        flex: 1,
        textAlign: 'center',
        width: '100%',
        color: '#515151',
        fontSize: 15,
        fontFamily: 'Roboto_500Medium',
        textAlign: 'left',
        maxWidth: 260,
        marginTop: 50
    },
    text: {
        flex: 0.2,
        textAlign: 'center',
        color: '#AEAEAE',
        fontSize: 14,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 260,
    },

    description: {
        color: '#6C6C80',
        fontSize: 16,
        marginTop: 16,
        fontFamily: 'Roboto_400Regular',
        maxWidth: 260,
        lineHeight: 24,
    },

    footer: {
        flex: 3,
        alignItems: 'center'
    },

    img: {
        marginTop: 30,
    },
    background: {
        backgroundColor: '#0E0E0E',
    },

    // input: {
    //   height: 60,
    //   backgroundColor: '#FFF',
    //   borderRadius: 10,
    //   marginBottom: 8,
    //   paddingHorizontal: 24,
    //   fontSize: 16,
    // },

    button: {
        justifyContent: 'center',
        backgroundColor: '#e48040',
        height: 60,
        width: 200,
        borderRadius: 10,
        color: 'white',
        flexDirection: 'row',
        overflow: 'hidden',
        alignItems: 'center',
        marginTop: 8,
    },

    buttonIcon: {
        height: 60,
        width: 60,
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
        justifyContent: 'center',
        alignItems: 'center'
    },

    buttonText: {
        flex: 1,
        justifyContent: 'center',
        textAlign: 'center',
        color: '#FFF',
        fontFamily: 'Roboto_500Medium',
        fontSize: 16,
    }
});

export default Home;