PGDMP  3    !                |            Workouts    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16927    Workouts    DATABASE     �   CREATE DATABASE "Workouts" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Workouts";
                postgres    false            �            1259    16940    routine_details    TABLE     �   CREATE TABLE public.routine_details (
    workout_title character varying(50) NOT NULL,
    split character varying(50),
    movement_type character varying(50),
    routine_spot character varying(50)
);
 #   DROP TABLE public.routine_details;
       public         heap    postgres    false            �          0    16940    routine_details 
   TABLE DATA           \   COPY public.routine_details (workout_title, split, movement_type, routine_spot) FROM stdin;
    public          postgres    false    217   �                  2606    16944 $   routine_details routine_details_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.routine_details
    ADD CONSTRAINT routine_details_pkey PRIMARY KEY (workout_title);
 N   ALTER TABLE ONLY public.routine_details DROP CONSTRAINT routine_details_pkey;
       public            postgres    false    217                       2606    16945    routine_details fk_exercise    FK CONSTRAINT     �   ALTER TABLE ONLY public.routine_details
    ADD CONSTRAINT fk_exercise FOREIGN KEY (workout_title) REFERENCES public.exercise_info(workout_title);
 E   ALTER TABLE ONLY public.routine_details DROP CONSTRAINT fk_exercise;
       public          postgres    false    217            �   %  x���M��0���)t���M<�I1	�	
�0��H�~���K�i;(L9[�3I�|O��9��9��������b}�q�e�Ջ�I�&(k8h��<t�$�4,�
�G��W���iE�WD�9��0
�xB�Z�����JQ�űgS��{�ދZ��Һ��hZ����8C�͘�4~��c�跱�96u��ְX�3B`�z�'�A䡺��ΰ�@@:��n��A?qC���)�Qki�8����iQ��\.�����݆@�e��F-S ��Yl\��)AQ�+�K�A�s�{������K���8Ir�B�-H�F!#�(VN5��׻!�`{�Zn�w�+��#g� ?�/�!�B�����x�����C��Աﭛi��>ف:�/Ў4f�@\ȩ¾�[�^	�g#���M|써)"����q���f�2)e+�	C>܋��&�̸9��4��Aӥ�*tQ&A}dW'�?�Ez����i�Tmt(>�s>��>�.~�|��8}�^탍T� R�ij�Ȟ�]EM.M��A�OR�̏O���7���     