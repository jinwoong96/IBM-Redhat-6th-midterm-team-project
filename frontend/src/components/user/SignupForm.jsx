import React, { useState } from 'react';
import { AtSign, Lock, TrendingUp, User } from 'lucide-react';
import { useNavigate } from 'react-router-dom'; 
import FormHeader from '../common/form/FormHeader';
import FormTextInput from '../common/form/FormTextInput';
import FormButton from '../common/form/FormButton';
import AuthFooter from '../common/form/AuthFooter';
import api from '../../api/api';

const SignupForm = () => {
    const navigate = useNavigate();
    
    const [formData, setFormData] = useState({
        user_id: '',
        user_nickname: '',
        user_password: '',
        password_check: ''
    });

    const [isSuccess, setIsSuccess] = useState(false);

    const handleChange = (e, field) => {
        setFormData({ ...formData, [field]: e.target.value });
    };

    const handleSignup = async (e) => {
        e.preventDefault();
        if (formData.user_password !== formData.password_check) {
            alert("비밀번호가 일치하지 않습니다.");
            return;
        }
        try {
            const payload = {
            login_id: formData.user_id,  
            user_nickname: formData.user_nickname,
            user_password: formData.user_password
            };

            const res = await api.post("/users", payload);

            if (res.data) {
                setIsSuccess(true);
            }
        } catch (error) {
            console.error("Signup Error:", error);
            alert(error.response?.data?.detail || "회원가입에 실패했습니다.");
        }
    };

    if (isSuccess) {
        return (
            <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white px-8 py-10 shadow-sm text-center">
                <TrendingUp className="mx-auto h-12 w-12 text-blue-500 mb-4" />
                <h2 className="text-2xl font-bold text-gray-800 mb-2">가입을 축하합니다!</h2>
                <p className="text-gray-600 mb-6">
                    축하합니다! <br />
                    <span className="font-bold text-blue-600">시드머니 5,000만원</span>이 지급되었습니다.
                </p>
                <button 
                    onClick={() => navigate('/login')}
                    className="w-full py-3 bg-blue-500 text-white rounded-xl font-semibold hover:bg-blue-600 transition-colors"
                >
                    로그인 하러가기
                </button>
            </div>
        );
    }

    return (
        <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white px-8 py-10 shadow-sm">
            <FormHeader 
                icon={<TrendingUp className="h-8 w-8 text-blue-500" />}
                title={"회원가입"}
                content={"투자 여정을 시작하세요"} 
            />
            <form className='mt-8 space-y-4' onSubmit={handleSignup}>
                <FormTextInput 
                    type={"text"} label={"아이디"} 
                    icon={<User className="mr-2 h-4 w-4 text-gray-400" />} 
                    placeholder={"kosdaqlover"} 
                    value={formData.login_id}
                    onChange={(e) => handleChange(e, 'user_id')}
                    
                />
                <FormTextInput 
                    type={"text"} label={"닉네임"} 
                    icon={<AtSign className="mr-2 h-4 w-4 text-gray-400"/>} 
                    placeholder={"코스닥러버"} 
                    value={formData.user_nickname}
                    onChange={(e) => handleChange(e, 'user_nickname')}
                />
                <FormTextInput 
                    type={"password"} label={"비밀번호"} 
                    icon={<Lock className="mr-2 h-4 w-4 text-gray-400"/>} 
                    placeholder={"••••••••"} 
                    value={formData.user_password}
                    onChange={(e) => handleChange(e, 'user_password')}
                />
                <FormTextInput 
                    type={"password"} label={"비밀번호 확인"} 
                    icon={<Lock className="mr-2 h-4 w-4 text-gray-400"/>} 
                    placeholder={"••••••••"} 
                    value={formData.password_check}
                    onChange={(e) => handleChange(e, 'password_check')}
                />
                <FormButton content={"가입하기"} type="submit" />
            </form>
            <AuthFooter type={"signup"} />
        </div>
    );
};

export default SignupForm;